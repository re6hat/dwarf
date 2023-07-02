#pragma once

#include<optional>

namespace dert {

class InlineClass
{
 public:
	InlineClass() { }
	explicit InlineClass(int input_) : _data(input_) { }

  const std::optional<int>& data() const { return _data; }

 private:
	std::optional<int> _data;
};

} // end of namespace dert
