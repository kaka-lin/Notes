# Overloading(重載) & Overriding (覆載) & Plymorphism (多型)

## Overloading (重載、多載):

在一個類別 (class) 中，多個名稱相同，但參數不同的 Method (方法)。

> 相同的方法名稱，擁有不同的實作。

```
相同名稱，參數型態或數目不同，但回傳型態要一樣
```

Example:

```c++
class Foo {
 public:
  void hello();
  void hello(int i);
  void hello(int i, int j) ;
  void hello(string s) ;
  void hello(int i, string s);
}
```

## Overriding (覆載):

是指子類別可以覆寫父類別的方法內容，使該方法擁有不同於父類別的行為。

```
【同型別】且【同參數】
```

Example:

```c++
class Animal {
 public:
  void foo() {
    cout << "This is from Animal" << endl;
  }
};

class Dog : public Animal {
 public:
  void foo() {
    cout << "This is from Dog" << endl;
  }
};

class Cat : public Animal {
 public:
  void foo() {
    cout << "This is from Cat" << endl;
  }
};
```

輸出:

```sh
This is from Animal
This is from Dog
This is from Cat
This is from Animal
```


## Polymorphism (多型): `以父類建立具有子類方法的物件`

是指父類別可透過子類別衍伸成多種型態，而父類別為子類別的通用型態，再透過子類別可覆寫父類別的方法來達到多型的效果，也就是同樣的方法名稱會有多種行為。

```
就是將子類別所有 overriding 的方法複製貼上到父類別的方法上。
如果子類別沒有複寫父類別方法，則會使用原來父類別方法
```

> ##### 1. 在 runtime 程式執行期間才決定要用哪一個實作，所以使用虛擬函式 (virtual function)
> ##### 2. 另外子類在 override 父類時，加上 override 關鍵字是個好習慣，使用 C++11 時編譯器在編譯階段可確保子類的函式的覆寫 override 是否成功，

Example:

```c++
class Animal {
 public:
  virtual void eat() {
    cout << "I eat food" << endl;
  }
};

class Dog : public Animal {
 public:
  virtual void eat() override {
    cout << "I eat meat" << endl;
  }
};

class Cat : public Animal {
 public:
  virtual void eat() override {
    cout << "I eat fish" << endl;
  }
};

class Unknown : public Animal {
};

int main() {
  // Polymorphism: 以父類建立具有子類方法的物件
  Animal* animal;
  Dog dog;
  Cat cat;
  Unknown u;

  animal = &dog;
  // virtual function, binded at runtime (Runtime polymorphism)
  animal->eat();
  // Non-virtual function, binded at compile time
  animal->foo();

  animal = &cat;
  animal->eat();
  animal->foo();

  animal = &u;
  animal->eat();
  animal->foo();

  return 0;
}
```

輸出如下:

```sh
I eat meat
This is from Animal
I eat fish
This is from Animal
I eat food
This is from Animal
```

根據多型的特性，使得我們可以在 runtime 程式執行期間再依據各種情形去選擇我們要用哪種子類，就像例子中的 dog 與 cat，如果有個新類別 Unknown 繼承了 Animal 類別沒有實作 eat() 時也能由父類的預設實作來代替。

## Reference

- [HabaCo/多型、覆寫、多載](https://gist.github.com/HabaCo/a2c8ed62efc1b5d42a1c)
- [Java 什麼是多載(Overload), 覆寫(Override), 多型(Polymorphism)](https://matthung0807.blogspot.com/2018/02/java-overload.html)
- [C++ virtual 的兩種用法](https://shengyu7697.github.io/cpp-virtual/)
- [Polymorphism in C++](https://www.geeksforgeeks.org/polymorphism-in-c/)
