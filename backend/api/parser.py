import pandas as pd
from .models import BoyName, GirlName, PopularName, Variant
import re


class CoreParser:
    def __init__(self, file_obj, sheet_name):
        self.sheet_name = sheet_name
        self.file_obj = file_obj
        self.df = None
        self.read_file()
        self.assign_names()
        self.assign_to_model_instance_and_save()

    @property
    def sheet_model_assigner(self):
        sheets = {
            "girlname": {"sheet_name": "girlnames", "model_name": GirlName},
            "boyname": {"sheet_name": "boynames", "model_name": BoyName},
            "popularname": {"sheet_name": "popular", "model_name": PopularName},
            "variant": {"sheet_name": "variants", "model_name": Variant},
        }

        return sheets

    def read_file(self):
        try:
            self.df = pd.read_excel(self.file_obj, sheet_name=self.sheet_model_assigner[self.sheet_name]["sheet_name"])
        except BaseException:
            print(Exception.args)

    def validate_data(self, row):
        raise NotImplementedError

    def assign_to_model_instance_and_save(self):
        raise NotImplementedError

    def assign_names(self):
        self.df.columns = self.names
        self.df = self.df.fillna("")


class NamesParser(CoreParser):
    def __init__(self, file_obj, sheet_name):
        super(NamesParser, self).__init__(file_obj, sheet_name)

    @property
    def rules(self):
        rules = {
            "name": str,
            "age_distribution_10": int,
            "age_distribution_20": int,
            "age_distribution_30": int,
            "age_distribution_50": int,
            "age_distribution_70": int,
            "age_distribution_71": int,
            "total_bearing_name": int,

            "average_age": int,
            "number_of_letters": str,
            # "double_name": bool,

            "frequency": str,
            "meaning": str
        }

        return rules

    @property
    def unique(self):
        unique = ["name"]

    @property
    def names(self):
        headers = [
            "name",
            "age_distribution_10",
            "age_distribution_20",
            "age_distribution_30",
            "age_distribution_50",
            "age_distribution_70",
            "age_distribution_71",
            "total_bearing_name",
            "average_age",
            "number_of_letters",
            "double_name",
            "frequency",
            "meaning",
        ]

        return headers

    def validate_data(self, row):
        print("validation row", row)
        for key in self.rules:
            if isinstance(row[key], self.rules[key]):
                # print(True)
                pass
            else:
                print(False)
                nv = re.findall(r'\d+', row[key])
                print(int(nv[0]))
                row[key] = int(nv[0])

        return row

    def assign_to_model_instance_and_save(self):
        data_to_save = []
        model = self.sheet_model_assigner[self.sheet_name]["model_name"]
        data = self.df.to_dict('records')
        print("data", data)
        for row in data:
            print("row", row["name"])
            row = self.validate_data(row=row)
            data_to_save.append(
                model(
                    name=row["name"],
                    age_distribution_10=row["age_distribution_10"],
                    age_distribution_20=row["age_distribution_20"],
                    age_distribution_30=row["age_distribution_30"],
                    age_distribution_50=row["age_distribution_50"],
                    age_distribution_70=row["age_distribution_70"],
                    age_distribution_71=row["age_distribution_71"],
                    total_bearing_name=row["total_bearing_name"],
                    average_age=row["average_age"],
                    number_of_letters=row["number_of_letters"],
                    double_name=row["double_name"],
                    frequency=row["frequency"],
                    meaning=row["meaning"]
                )
            )
        print(data_to_save)
        model.objects.bulk_create(data_to_save)


class PopularParser(CoreParser):
    def __init__(self, file_obj, sheet_name):
        super(PopularParser, self).__init__(file_obj, sheet_name)

    @property
    def rules(self):
        rules = {
            "year": int,
            "name": str,
            "gender": str,
            "position": int
        }

        return rules

    @property
    def names(self):
        names = [
            "year",
            "position",
            "name",
            "gender",
        ]

        return names

    def assign_to_model_instance_and_save(self):
        data_to_save = []
        model = self.sheet_model_assigner[self.sheet_name]["model_name"]
        data = self.df.to_dict('records')
        print(model)
        for row in data:
            print(row)
            #     # row = self.validate_data(row=row)
            data_to_save.append(
                model(
                    year=row["year"],
                    name=row["name"],
                    gender=row["gender"],
                    position=row["position"]
                )
            )
        print(data_to_save)
        model.objects.bulk_create(data_to_save)

    def validate_data(self, row):
        pass


class VariantsParser(CoreParser):
    def __init__(self, file_obj, sheet_name):
        super(VariantsParser, self).__init__(file_obj, sheet_name)

    @property
    def rules(self):
        rules = {
            "name": str,
            "language": str,
            "variants": str
        }

        return rules

    @property
    def names(self):
        names = [
            "name",
            "language",
            "variants"
        ]

        return names

    def assign_to_model_instance_and_save(self):
        data_to_save = []
        model = self.sheet_model_assigner[self.sheet_name]["model_name"]
        data = self.df.to_dict('records')
        print(model)
        for row in data:
            print(row)
        #     # row = self.validate_data(row=row)
            data_to_save.append(
                model(
                    name=row["name"],
                    language=row["language"],
                    variants=row["variants"]
                )
            )
        print(data_to_save)
        model.objects.bulk_create(data_to_save)

    def validate_data(self, row):
        pass


def dispatcher(name):
    parsers = {
        "girlname": NamesParser,
        "boyname": NamesParser,
        "popularname": PopularParser,
        "variant": VariantsParser
    }

    return parsers[name]
