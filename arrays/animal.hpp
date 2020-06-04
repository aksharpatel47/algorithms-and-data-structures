#if !defined(ANIMAL)
#define ANIMAL

#include <string>
#include <iostream>

class Animal
{
private:
    std::string name;
    double height;
    double weight;

    static inline int numOfAnimals = 0;

public:
    Animal(std::string name, double height, double weight);
    ~Animal();

    std::string GetName() { return name; }
    void SetName(std::string name) { this->name = name; }
    double GetHeight() { return height; }
    void SetHeight(double height) { this->height = height; }
    double GetWeight() { return weight; }
    void SetWeight(double weight) { this->weight = weight; }

    void SetAll(std::string, double, double);

    void ToString();
};

void Animal::SetAll(std::string name, double height, double weight)
{
    this->name = name;
    this->height = height;
    this->weight = weight;
}

Animal::Animal(std::string name, double height, double weight)
{
    SetAll(name, height, weight);

    Animal::numOfAnimals += 1;
}

Animal::~Animal()
{
    std::cout << Animal::numOfAnimals << " animals." << std::endl;
    std::cout << "Animal " << this->name << " destroyed." << std::endl;
    Animal::numOfAnimals -= 1;
}

void Animal::ToString()
{
    std::cout << this->name << " is " << this->height << " cms tall and " << this->weight << " kgs in weight." << std::endl;
}

#endif // ANIMAL
