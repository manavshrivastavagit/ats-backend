""" Defines the HR repository """

from models import HR


class HRRepository:
    """ The repository for the HR model """

    @staticmethod
    def get(last_name, first_name):
        """ Query a HR by last and first name """
        return HR.query.filter_by(last_name=last_name, first_name=first_name).one()

    def update(self, last_name, first_name):
        """ Update a HR's age """
        HR = self.get(last_name, first_name)
        # HR.age = age

        return HR.save()

    @staticmethod
    def create(last_name, first_name):
        """ Create a new HR """
        newHR = HR(last_name=last_name, first_name=first_name)

        return newHR.save()
