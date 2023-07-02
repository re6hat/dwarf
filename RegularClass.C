#include "RegularClass.H"

namespace dert {

RegularClass::RegularClass()
{ }

RegularClass::RegularClass(int input_)
	: _data(input_)
{ }

const std::optional<int>& RegularClass::data() const
{
	return _data;
}

} // end of namespace dert
