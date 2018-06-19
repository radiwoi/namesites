import pandas as pd
from .models import BoyName, GirlName, PopularName, Variant
import re
# from .views import LowerCase


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        for z in l[i:i + n]:
            yield z


class CoreParser:
    def __init__(self, file_obj, sheet_name):
        self.sheet_name = sheet_name
        self.file_obj = file_obj
        self.df = None
        # todo check if we need this
        self.model = None
        self.to_update = None

    @property
    def sheet_model_assigner(self):
        sheets = {
            "girlname": {"sheet_name": "girlnames", "model_name": GirlName},
            "boyname": {"sheet_name": "boynames", "model_name": BoyName},
            "popularname": {"sheet_name": "popular", "model_name": PopularName},
            "variant": {"sheet_name": "variants", "model_name": Variant},
        }

        return sheets

    def parse(self):
        """
        runs and control parsing process
        @todo: write exceptions handler
        :return: parsing result
        """
        self.read_file()
        self.assign_names()
        result = self.assign_to_model_instance_and_save()

        return result

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

        return unique

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
        # print("validation row", row)

        if row["name"].lower() in self.to_update:
            # print("EXISTS!")
            return False

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

    def check_existing(self):
        self.to_update = [item.lower() for item in self.model.objects.values_list('name', flat=True)]

    def assign_to_model_instance_and_save(self):
        data_to_save = []
        model = self.sheet_model_assigner[self.sheet_name]["model_name"]
        # todo remove or rewrite this
        self.model = model
        self.check_existing()

        # return False
        data = self.df.to_dict('records')
        # print("data", data)
        for row in data:
            # print("row", row["name"])
            row = self.validate_data(row=row)
            if not row:
                continue

            self.to_update.append(row["name"].lower())

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
        # print(data_to_save)
        reason = ""
        if len(data_to_save) == 0:
            reason = "No unique records"
        model.objects.bulk_create(data_to_save)

        for name in chunks(l=model.objects.all(), n=100):
            variants = Variant.objects.filter(name=name.name).all()
            print(variants)
            name.variants.add(*variants)

        return len(data_to_save), reason


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
        # data_to_save = []
        # model = self.sheet_model_assigner[self.sheet_name]["model_name"]
        # data = self.df.to_dict('records')
        # print(model)
        # for row in data:
        #     print(row)
        #     #     # row = self.validate_data(row=row)
        #     data_to_save.append(
        #         model(
        #             year=row["year"],
        #             name=row["name"],
        #             gender=row["gender"],
        #             position=row["position"]
        #         )
        #     )
        # print(data_to_save)
        # model.objects.bulk_create(data_to_save)
        #
        # return len(data_to_save), ""
        data_to_save = []
        self.df = self.df.reset_index()
        print(self.df)
        # return
        model = self.sheet_model_assigner[self.sheet_name]["model_name"]
        data = self.df.to_dict('records')
        print(model)
        for row in data:
            row_dict = {
                "year": row["year"],
                "position": row["position"],
            }
            # print(row)

            popular = model.objects.filter(**row_dict).first()

            if popular is None:
                popular = model(
                    **row_dict
                )

                popular.save()

            if row['gender'] == 'boy':
                boy_name = BoyName.objects.filter(name__iexact=row["name"]).first()
                if boy_name is not None:
                    boy_name.popular.add(popular)
            else:
                girl_name = GirlName.objects.filter(name__iexact=row["name"]).first()
                if girl_name is not None:
                    girl_name.popular.add(popular)

        return len(data_to_save), ""

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
        self.df = self.df.reset_index()
        mapped_data = self.df["variants"].str.split(",")
        mapped_data = mapped_data.apply(pd.Series, 1).stack().map(lambda v: v.strip())
        mapped_data.index = mapped_data.index.droplevel(-1)
        mapped_data.name = 'variant_name'
        self.df = self.df.join(mapped_data)
        print(self.df)
        del mapped_data
        # return
        model = self.sheet_model_assigner[self.sheet_name]["model_name"]
        data = self.df.to_dict('records')
        del self.df

        # existing_variants = model.objects.values("language", "name")

        # print(existing_variants)
        # return

        # print(model)
        for row in data:
            row_dict = {
                "language": row["language"],
                "name": row["variant_name"]
            }
            # print(row_dict)

            variant = model.objects.filter(**row_dict).first()

            # if row['name'] == 'Abraham' and row['language'] == 'Arabiska':
            #     print(variant)
            #     print(BoyName.objects.filter(name__lower=row["name"]).query)
            #     boy_name = BoyName.objects.filter(name__lower=row["name"]).first()
            #     print(boy_name)

            if variant is None:
                variant = model(
                    **row_dict
                )

                variant.save()

            boy_name = BoyName.objects.filter(name__lower=row["name"].lower()).first()
            girl_name = GirlName.objects.filter(name__lower=row["name"].lower()).first()
            if boy_name is not None:
                boy_name.variants.add(variant)
            if girl_name is not None:
                girl_name.variants.add(variant)
        print(data_to_save)

        # model.objects.bulk_create(data_to_save)
        return len(data_to_save), ""

    def validate_data(self, row):
        pass


def dispatcher(name, file, model):
    """
    creates and returns parser instance
    :param name: Parser className
    :param file: File to parse
    :param model: model to update
    :return: Parser class instance
    """
    parsers = {
        "girlname": NamesParser,
        "boyname": NamesParser,
        "popularname": PopularParser,
        "variant": VariantsParser
    }

    return parsers[name](file_obj=file, sheet_name=model)
