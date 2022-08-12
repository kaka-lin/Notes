#include <iostream>
#include <string>

using namespace std;

// Overloading
class Greet {
 public:
  void hello() {cout << "Hello" << endl;};
  void hello(int i);
  void hello(int i, int j) ;
  void hello(string s) {
    cout << "Hello, " << s << endl;
  };
  void hello(int i, string s);
};

// Overriding
class Animal {
 public:
  void foo() {
    cout << "This is from Animal" << endl;
  }

  virtual void eat() {
    cout << "I eat food (Animal)" << endl;
  }
};

class Dog : public Animal {
 public:
  void foo() {
    cout << "This is from Dog" << endl;
  }

  virtual void eat() override {
    cout << "I eat meat (Dog)" << endl;
  }
};

class Cat : public Animal {
 public:
  void foo() {
    cout << "This is from Cat" << endl;
  }

  virtual void eat() override {
    cout << "I eat fish (Cat)" << endl;
  }
};

class Unknown : public Animal {
};

int main() {
  // Overloading
  cout << "=== Overloading ===" << endl;
  Greet greet;
  greet.hello();
  greet.hello("kaka");


  // Overriding
  cout << "=== Overriding ===" << endl;
  Animal animal;
  Dog dog;
  Cat cat;
  Unknown u;
  animal.foo();
  dog.foo();
  cat.foo();
  u.foo();

  // Polymorphism: 以父類建立具有子類方法的物件
  cout << "=== Polymorphism ===" << endl;
  Animal* animal2;

  animal2 = &dog;
  // virtual function, binded at runtime (Runtime polymorphism)
  animal2->eat();
  // Non-virtual function, binded at compile time
  animal2->foo();

  animal2 = &cat;
  // virtual function, binded at runtime (Runtime polymorphism)
  animal2->eat();
  // Non-virtual function, binded at compile time
  animal2->foo();

  animal2 = &u;
  // virtual function, binded at runtime (Runtime polymorphism)
  animal2->eat();
  // Non-virtual function, binded at compile time
  animal2->foo();

  return 0;
}
