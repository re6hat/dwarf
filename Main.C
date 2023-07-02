#include "A.H"
#include "B.H"
#include "RegularFunction.H"
#include "RegularClass.H"
#include "InlineFunction.H"
#include "InlineClass.H"

#include <iostream>

using namespace dert;

int main(int argc, char *argv[])
{
	// template functions
	{
		std::cout << "template functions ..." << std::endl;

		std::string s{"abc"};
		int i = 100;

		auto opts = toOptStr(s);
		auto opti = toOptInt(i);

		std::cout << "opts=" << *opts << ", opts=" << *opti << std::endl;
	}

  // template classes
	{
		std::cout << "template classes ..." << std::endl;

		StrClass sc("abc");
		IntClass ic(100);

		std::cout << "StrClass=" << getData(sc) << ", IntClass=" << getData(ic) << std::endl;
	}

  // regular functions
	{
		std::cout << "regular functions ..." << std::endl;

		std::cout << regularFunction()  << std::endl;
	}

  // regular classes
	{
		std::cout << "regular classes ..." << std::endl;

		RegularClass rc(99);
		std::cout << "rc=" << *(rc.data()) << std::endl;
	}

	// inline functions
	{
		std::cout << "inline functions ..." << std::endl;

		std::cout << inlineFunction() << std::endl;
  }

	// weak functions
	{
		std::cout << "weak functions ..." << std::endl;

		std::cout << weakFunction() << std::endl;
  }

	// inline classes
	{
		std::cout << "inline classes ..." << std::endl;

		InlineClass ic(98);
    std::cout << "ic=" << *(ic.data()) << std::endl;
	}

	return 0;
}
