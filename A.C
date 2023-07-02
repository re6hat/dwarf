#include "A.H"

namespace dert {

std::optional<int> toOptInt(const int& input_)
{
	return makeOptional(input_);
}

const int& getData(const IntClass& input_)
{
	return input_.data();
}

} // end of namespace dert
