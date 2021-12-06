import enum


class BaseEnum(enum.Enum):

    @classmethod
    def get_by_value(cls, value):
        return next(filter(lambda x: x.value == value, cls))


class KeywordsEnum(BaseEnum):
    def __init__(self, *args):
        self._value_, self.keywords = args

    @classmethod
    def get_by_value(cls, value):
        """
        Get enum item by lowercase value matching

        Args:
            value -- (str) Raw value
        Returns:
            (KeywordsEnum|None) -- Return matched enum item or None
        """
        matches = list(filter(lambda x: x.value.lower() == value.lower(), cls))
        return matches[0] if matches else None

    @classmethod
    def get_by_keywords(cls, value, min_match=None):
        """
        Get enum item by checking keywords match

        Parameters
        ----------
        value:str
            Value to look for in the current enum
        min_match:int
            Min number of keywords to match, all by default
        Returns
        -------
            KeywordsEnum|None: Return matched enum item or None
        """

        def has_all_keywords(keywords):
            # Return True if raw value includes all keywords
            return len([k for k in keywords if k == value.lower()])

        # Get all matches with enum items keywords
        matches = list(filter(lambda x: has_all_keywords(x.keywords), cls))
        if len(matches) > 1:
            return matches[0]
        elif not matches:
            if min_match is not None:
                return None
        else:
            return matches[0]
