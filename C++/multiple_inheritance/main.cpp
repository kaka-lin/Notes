#include <iostream>

using namespace std;

class A
{
    public:
        virtual void func()
        {
            cout << "function form A" << endl;
        }
};

class B : virtual public A
{
    public:
        void func()
        {
            cout << "function form B" << endl;
            //A::func();
        }
};

class C : virtual public A
{
    public:
        void func()
        {
            cout << "function form C" << endl;
            //A::func();
        }
};

class D : public B, public C
{
    public:
        void func()
        {
            // use the func() of class B
            B::func();

            // use the func() of class C
            C::func();

            // use the func() of class A
            B::A::func();
        }
};

int main()
{
    D d;
    d.func();

    return 0;
}
