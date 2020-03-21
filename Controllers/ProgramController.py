


class ProgramController:
    def __init__(self):
        pass

    @staticmethod
    def get_user_input():
        user_input = ""
        try:
            user_input = input("type your country: ")
            return user_input
        except Exception as err:
            print(f"Invalid input, error message: {err}")

    @staticmethod
    def show_data(countryModel):
        relative_cases = str(countryModel.relative_cases())
        absolute_cases = str(countryModel.absolute_cases())
        return {"relative_cases" :relative_cases, "absolute_cases" :absolute_cases}
