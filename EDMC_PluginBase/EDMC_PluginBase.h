#pragma once

using namespace System;

struct inArg
{
	char* edmcSysName;
	int testVal1;
	float testVal2;
};

extern "C" __declspec(dllexport) void __stdcall Init();
extern "C" __declspec(dllexport) void __stdcall Update(inArg* _inArg);
extern "C" __declspec(dllexport) void __stdcall Closing();