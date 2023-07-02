#pragma once

#include <stdlib.h>

namespace dert {

inline int inlineFunction()
{
	return rand();
}

int weakFunction() __attribute__((weak, noinline));

int weakFunction()
{
	return rand();
}

} // end of namespace dert
