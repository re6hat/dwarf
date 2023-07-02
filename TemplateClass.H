#pragma once

namespace dert {

template <typename T>
class TemplateClass
{
 public:
  TemplateClass(const T& input_)
	 : _data(input_)
	{ }

	const T& data() const
	{
		return _data;
	}

 private:
	T _data;
};

} // end of namespace dert
