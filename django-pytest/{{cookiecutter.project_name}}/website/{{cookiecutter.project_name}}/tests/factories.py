import factory

from {{cookiecutter.project_name}}.models import Person


class PersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Person

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    company = factory.Faker('company')
    address = factory.Faker('street_address')
    city = factory.Faker('city')
    postal_code = factory.Faker('postcode')

    email = factory.LazyAttributeSequence(
        lambda o, n: '%s%s@example.com' % (o.first_name[0], o.last_name)
    )
