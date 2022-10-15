#ifndef INTERPRETER_H_INCLUDED
#define INTERPRETER_H_INCLUDED

#include "lang.hpp"
#include <unordered_map>
#include <string>
struct res_prog;
void free_res_prog(struct res_prog* r);
void free_cont_list(struct cont_list* cl);
struct res_prog * init_res_prog(struct cmd * c, std::unordered_map<std::string, long long int>* globals);
void step(struct res_prog * r);
int test_end(struct res_prog *&r);

#endif
