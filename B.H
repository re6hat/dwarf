#pragma once

#include "TemplateFunction.H"
#include "TemplateClass.H"
#include "RegularFunction.H"
#include "RegularClass.H"
#include "InlineFunction.H"
#include "InlineClass.H"

#include <string>

namespace dert {

std::optional<std::string> toOptStr(const std::string& input_);

using StrClass = TemplateClass<std::string>;

const std::string& getData(const StrClass& input_);

} // end of namespace dert
