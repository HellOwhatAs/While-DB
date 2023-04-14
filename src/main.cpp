#include <stdio.h>
#include "lang.hpp"
#include "lexer.hpp"
#include "parser.hpp"
#include "interpreter.hpp"
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/stl_bind.h>
#include <stdexcept>
namespace py = pybind11;
extern struct cmd* root;
int yyparse();

PYBIND11_MAKE_OPAQUE(std::unordered_map<std::string, long long int>);
std::unordered_map<std::string, long long int> globals;
res_prog* r=NULL;
bool no_program = true;
PYBIND11_MODULE(_WhileDB, m) {
	m.def("load_program", [](const std::string& src, bool exec_to_end) {
		if (!no_program)free_cmd(root);
		no_program = false;
		if (r != NULL) { free_res_prog(r); r = NULL; }
		auto db = yy_scan_string(src.c_str());
		yy_switch_to_buffer(db);
		yyparse();
		yy_delete_buffer(db);
		r = init_res_prog(root, &globals);
		if (exec_to_end)while (!test_end(r))step(r);
	}, py::arg("src"), py::arg("exec_to_end") = true);
	m.def("end", []() {
		if (no_program)throw std::logic_error("no program loaded");//py::value_error("no program loaded");
		if (r == NULL)return true;
		return (bool)test_end(r); 
	});
	m.def("step", []() {
		if (no_program)throw std::logic_error("no program loaded");//py::value_error("no program loaded");
		if (r == NULL)throw std::logic_error("no program loaded");//py::value_error("no more step");
		step(r); 
	});
	py::bind_map<std::unordered_map<std::string, long long int>>(m, "Unordered_MapStringInt");
	m.def("Globals", [](){return &globals;}, py::return_value_policy::reference);
	m.def("to_end", []() {
		if (no_program)throw std::logic_error("no program loaded");//py::value_error("no program loaded");
		while (!test_end(r))step(r);
	});
}