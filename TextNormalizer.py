class TextNormalizer:


    def removepunct(self, text):
        text = text.replace('(', '')\
            .replace("'", '')\
            .replace(',', '')\
            .replace('[', '')\
            .replace(']', '')\
            .replace('.', '')\
            .replace('"', '')\
            .replace('/', '')\
            .replace(')', '')\
            .replace('(', '')\
            .replace(';', '')\
            .replace('?', '')\
            .replace('!', '')\
            .replace('-', ' ')\
            .replace('?', '')\
            .replace('"', '')\
            .replace('*', '')\
            .replace('+', '')\
            .replace('=', '')\
            .replace('-', '')\
            .replace('_', '')\
            .replace('#', '')\
            .replace('@', '')\
            .replace('>', '')\
            .replace('}', '')\
            .replace('{', '')\
            .replace(':', '')
        return text

    def removenumb(self, text):
        table = str.maketrans(dict.fromkeys('1234567890'))
        text = text.translate(table)
        return  text

    def normalizing(self, text):
        text = self.removepunct(text)
        text = self.removenumb(text)

        return text