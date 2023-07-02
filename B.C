#include "B.H"

namespace dert {

std::optional<std::string> toOptStr(const std::string& input_)
{
	return makeOptional(input_);
}

const std::string& getData(const StrClass& input_)
{
	return input_.data();
}

} // end of namespace dert
