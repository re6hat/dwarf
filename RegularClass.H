#pragma once

#include<optional>

namespace dert {

class RegularClass
{
 public:
	RegularClass();
	explicit RegularClass(int input_);

  const std::optional<int>& data() const;

 private:
	std::optional<int> _data;
};

} // end of namespace
