import re
from typing import Optional, Tuple, Set


class CitiesHelper:
    """
    Вспомогательный класс для игры в города.
    Все методы статические — не требует создания экземпляра.
    """

    @staticmethod
    def get_last_significant_letter(city: str) -> str:
        """
        Возвращает последнюю значимую букву названия города.

        Правила:
        - Если город оканчивается на 'ъ' или 'ь', берётся предпоследняя буква.
        - В противном случае возвращается последняя буква.

        Args:
            city: Название города (строка)

        Returns:
            Последняя значимая буква в нижнем регистре.
            Если город пустой или не содержит букв — возвращает пустую строку.

        Примеры:
            >>> CitiesHelper.get_last_significant_letter("Казань")
            'н'
            >>> CitiesHelper.get_last_significant_letter("Москва")
            'а'
            >>> CitiesHelper.get_last_significant_letter("Пермь")
            'м'
            >>> CitiesHelper.get_last_significant_letter("Шахты")
            'т'
        """

        # Убираем всё, кроме букв (чтобы дефисы и апострофы не мешали)
        city_clean = CitiesHelper._clean_city(city)

        if not city_clean:
            return ''

        # Последняя буква
        last_char = city_clean[-1]

        # Если последняя буква - 'ъ' или 'ь', берём предпоследнюю
        if last_char in ['ъ', 'ь', 'ы']:
            if len(city_clean) >= 2:
                return city_clean[-2]
            else:
                return ''  # Случай, когда город состоит только из 'ь' или 'ъ' (такого быть не может)

        return last_char

    @staticmethod
    def get_first_letter(city: str) -> str:
        """
        Возвращает первую значимую букву названия города.

        Args:
            city: Название города (строка)

        Returns:
            Первая буква города в нижнем регистре.
            Если город пустой или не содержит букв — возвращает пустую строку.

        Примеры:
            >>> CitiesHelper.get_first_letter("Москва")
            'м'
            >>> CitiesHelper.get_first_letter("Йошкар-Ола")
            'й'
        """
        cleaned = CitiesHelper._clean_city(city)
        return cleaned[0] if cleaned else ''

    @staticmethod
    def is_valid_next_city(previous_city: str, new_city: str) -> bool:
        """
        Проверяет, можно ли назвать новый город после предыдущего.

        Args:
            previous_city: Название предыдущего города
            new_city: Название нового города

        Returns:
            True, если новый город начинается на последнюю значимую букву предыдущего.

        Примеры:
            >>> CitiesHelper.is_valid_next_city("Казань", "Новгород")
            True
            >>> CitiesHelper.is_valid_next_city("Москва", "Архангельск")
            True
            >>> CitiesHelper.is_valid_next_city("Рязань", "Ярославль")
            False
        """
        if not previous_city or not new_city:
            return False

        required_letter = CitiesHelper.get_last_significant_letter(previous_city)
        if not required_letter:
            return False

        first_letter = CitiesHelper.get_first_letter(new_city)
        if not first_letter:
            return False

        return first_letter == required_letter

    @staticmethod
    def _clean_city(city: str) -> str:
        """
        Внутренний метод для очистки названия города.
        Удаляет всё, кроме букв (включая латиницу для поддержки иностранных названий).
        Приводит к нижнему регистру.
        """
        if not city:
            return ''

        city = city.lower()
        # Удаляем всё, кроме букв (русских и латинских)
        cleaned = re.sub(r'[^а-яё]', '', city)
        return cleaned


    @staticmethod
    def is_city_repeated(city: str, used_cities: set) -> bool:
        """
        Проверяет, был ли уже назван этот город.

        Args:
            city: Название города для проверки
            used_cities: Множество уже использованных городов

        Returns:
            True, если город уже есть в списке использованных, иначе False

        Примеры:
            >>> used = {"москва", "казань", "новгород"}
            >>> CitiesHelper.is_city_repeated("Москва", used)
            True
            >>> CitiesHelper.is_city_repeated("Новгород", used)
            True
            >>> CitiesHelper.is_city_repeated("Санкт-Петербург", used)
            False
            >>> CitiesHelper.is_city_repeated("", used)
            False
        """
        if not city or not used_cities:
            return False

        cleaned = CitiesHelper._clean_city(city)
        return cleaned in used_cities

# ========== Примеры использования ==========
if __name__ == "__main__":
    # Тестирование
    print("=== Базовые функции ===\n")
    print(CitiesHelper.get_last_significant_letter("пермь"))