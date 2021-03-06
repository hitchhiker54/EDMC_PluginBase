#include "stdafx.h"

#include "EDMC_PluginBase.h"

/*
	A barebones framework to customise and pass on EDMC data to .NET or native code
*/

void __stdcall Init()
{
	Console::WriteLine("DLL Init called.");
}

void __stdcall Update(inArg* _inArg)
{
	Console::WriteLine("DLL Update called.");

	String^ systemName = gcnew String(_inArg->edmcSysName);
	Console::WriteLine(systemName);
	Console::WriteLine(_inArg->testVal1.ToString());
	Console::WriteLine(_inArg->testVal2.ToString());
}

void __stdcall Closing()
{
	Console::WriteLine("DLL Closing called.");
}