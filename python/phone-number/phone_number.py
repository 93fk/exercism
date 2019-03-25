import re
number_pattern = r"(\+1)?\s*[(]?[2-9]{1}\d{2}[)]?\s*[-.]?\s*[2-9]{1}\d{2}\s*[-.]?\s*\d{4}"
class Phone(object):
      

    def __init__(self, phone_number):
        if re.match(number_pattern, phone_number) is None:
            raise(ValueError('The number format is invalid.'))
        else:
            number = ''.join(re.findall(r'\d{3,10}', phone_number))
            self.number = number
            self.area_code = number[:3]

    def pretty(self):
        n = self.number
        return f'({n[:3]}) {n[3:7]}-{n[7:]}'