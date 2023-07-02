#pragma once

#include "TemplateFunction.H"
#include "TemplateClass.H"
#include "RegularFunction.H"
#include "RegularClass.H"
#include "InlineFunction.H"
#include "InlineClass.H"

namespace dert {

std::optional<int> toOptInt(const int& input_);

using IntClass = TemplateClass<int>;

const int& getData(const IntClass& input_);

} // end of namespace dert
