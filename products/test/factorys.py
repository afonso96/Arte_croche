import factory
import factory.fuzzy


from ..models import Category, Product


class CategoryFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()

    class Meta:
        model = Category


class ProductFactory(factory.django.DjangoModelFactory):
    category = factory.SubFactory(CategoryFactory)
    name = factory.fuzzy.FuzzyText()
    image = factory.django.ImageField()
    description = factory.Faker("paragraph", nb_sentences=3, variable_nb_setences=True)
    price = factory.fuzzy.FuzzyDecimal(5.0, 999.99)
    is_avaliable = factory.Faker("pyboll")

    class Meta:
        model = Product