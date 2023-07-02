#pragma once

#include <string>
#include <optional>

namespace dert {

template<typename T>
std::optional<T> makeOptional(const T& input_)
{
	return {input_};
}

} // end of namespace dert
