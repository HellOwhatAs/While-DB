#include <stdio.h>
#include "lang.hpp"
#include "lexer.hpp"
#include "parser.hpp"
#include "interpreter.hpp"
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
namespace py = pybind11;
extern struct cmd* root;
int yyparse();

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
		if (no_program)throw py::value_error("no program loaded");
		if (r == NULL)return true;
		return (bool)test_end(r); 
	});
	m.def("step", []() {
		if (no_program)throw py::value_error("no program loaded");
		if (r == NULL)throw py::value_error("no more step");
		step(r); 
	});
	m.def("get_globals", []() {return globals; });
	m.def("update_globals", [](const std::unordered_map<std::string, long long int>& d) {for (auto& i : d)globals[i.first] = i.second; });
	m.def("clear_globals", []() {globals.clear(); });
	m.def("to_end", []() {
		if (no_program)throw py::value_error("no program loaded");
		while (!test_end(r))step(r);
	});
}