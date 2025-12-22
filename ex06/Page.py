from elem import Elem, Text
from elements import *


class Page:

    def __init__(self, elem: Elem):
        self.elem = elem

    def is_valid(self):
        if not (
            type(self.elem) == Html
            or type(self.elem) == Head
            or type(self.elem) == Body
            or type(self.elem) == Title
            or type(self.elem) == Meta
            or type(self.elem) == Img
            or type(self.elem) == Table
            or type(self.elem) == Th
            or type(self.elem) == Tr
            or type(self.elem) == Td
            or type(self.elem) == Ul
            or type(self.elem) == Ol
            or type(self.elem) == Li
            or type(self.elem) == H1
            or type(self.elem) == H2
            or type(self.elem) == P
            or type(self.elem) == Div
            or type(self.elem) == Span
            or type(self.elem) == Hr
            or type(self.elem) == Br
        ):
            return False

        if type(self.elem) == Html and (
            len(self.elem.content) != 2
            or not type(self.elem.content[0]) == Head
            or not type(self.elem.content[1]) == Body
        ):
            return False

        if type(self.elem) == Head and (
            len(self.elem.content) != 1 or not type(self.elem.content[0]) == Title
        ):
            return False

        if type(self.elem) == Body or type(self.elem) == Div:
            for elem in self.elem.content:
                if (
                    type(elem) != H1
                    and type(elem) != H2
                    and type(elem) != Div
                    and type(elem) != Table
                    and type(elem) != Ul
                    and type(elem) != Ol
                    and type(elem) != Span
                    and type(elem) != Text
                ):
                    return False

        if (
            type(self.elem) == Title
            or type(self.elem) == H1
            or type(self.elem) == H2
            or type(self.elem) == Li
            or type(self.elem) == Th
            or type(self.elem) == Td
        ) and (len(self.elem.content) != 1 or not type(self.elem.content[0]) == Text):
            return False

        if type(self.elem) == P:
            for elem in self.elem.content:
                if type(elem) != Text:
                    return False

        if type(self.elem) == Span:
            for elem in self.elem.content:
                if type(elem) != Text and type(elem) != P:
                    return False

        if type(self.elem) == Ul or type(self.elem) == Ol:
            if len(self.elem.content) == 0:
                return False
            for elem in self.elem.content:
                if type(elem) != Li:
                    return False

        if type(self.elem) == Tr:
            if len(self.elem.content) == 0:
                return False
            if type(self.elem.content[0]) == Th:
                for elem in self.elem.content:
                    if type(elem) != Th:
                        return False
            elif type(self.elem.content[0]) == Td:
                for elem in self.elem.content:
                    if type(elem) != Td:
                        return False

        if type(self.elem) == Table:
            for elem in self.elem.content:
                if type(elem) != Tr:
                    return False

        for elem in self.elem.content:
            if type(elem) != Text and not Page(elem).is_valid():
                return False

        return True

    def __str__(self):
        if type(self.elem) == Html:
            return f"<!DOCTYPE html>\n{str(self.elem)}"

        return str(self.elem)

    def write_to_file(self, filename: str):
        try:
            with open(filename, "w") as file:
                file.write(str(self))
        except Exception as e:
            print(f"Error writing to file {filename}: {e}")


if __name__ == "__main__":
    html = Html(
        [
            Head(Title(Text("Test Page"))),
            Body(
                [
                    H1(Text("Hello World")),
                    P(Text("This is a test paragraph.")),
                    Div(
                        [
                            H2(Text("Section")),
                            Ul([Li(Text("Item 1")), Li(Text("Item 2"))]),
                        ]
                    ),
                    Table(
                        [
                            Tr([Th(Text("Header 1")), Th(Text("Header 2"))]),
                            Tr([Td(Text("Data 1")), Td(Text("Data 2"))]),
                        ]
                    ),
                ]
            ),
        ]
    )
    page = Page(html)
    print("Valid HTML page test:")
    print("is_valid():", page.is_valid())
    print("HTML output:")
    print(page)
    page.write_to_file("test_valid.html")
    print("Written to test_valid.html\n")

    html_invalid = Html([Body(H1(Text("Hello")))])
    page_invalid = Page(html_invalid)
    print("Invalid HTML page test (missing Head):")
    print("is_valid():", page_invalid.is_valid())
    print()

    html_extra = Html(
        [Head(Title(Text("Test"))), Body(H1(Text("Hello"))), Div(Text("Extra"))]
    )
    page_extra = Page(html_extra)
    print("Invalid HTML page test (extra content):")
    print("is_valid():", page_extra.is_valid())
    print()

    head_invalid = Head(P(Text("Not a title")))
    page_head_invalid = Page(head_invalid)
    print("Invalid Head test (missing Title):")
    print("is_valid():", page_head_invalid.is_valid())
    print()

    head_valid = Head(Title(Text("Valid Title")))
    page_head_valid = Page(head_valid)
    print("Valid Head test:")
    print("is_valid():", page_head_valid.is_valid())
    print()

    body_invalid = Body(Meta())
    page_body_invalid = Page(body_invalid)
    print("Invalid Body test (invalid content):")
    print("is_valid():", page_body_invalid.is_valid())
    print()

    body_valid = Body([H1(Text("Title")), P(Text("Para"))])
    page_body_valid = Page(body_valid)
    print("Valid Body test:")
    print("is_valid():", page_body_valid.is_valid())
    print()

    title_valid = Title(Text("Title"))
    page_title_valid = Page(title_valid)
    print("Valid Title test:")
    print("is_valid():", page_title_valid.is_valid())
    print()

    title_invalid = Title(H1(Text("Not text")))
    page_title_invalid = Page(title_invalid)
    print("Invalid Title test (not Text):")
    print("is_valid():", page_title_invalid.is_valid())
    print()

    p_valid = P(Text("Paragraph"))
    page_p_valid = Page(p_valid)
    print("Valid P test:")
    print("is_valid():", page_p_valid.is_valid())
    print()

    p_invalid = P(H1(Text("Not text")))
    page_p_invalid = Page(p_invalid)
    print("Invalid P test (not Text):")
    print("is_valid():", page_p_invalid.is_valid())
    print()

    ul_valid = Ul([Li(Text("Item"))])
    page_ul_valid = Page(ul_valid)
    print("Valid Ul test:")
    print("is_valid():", page_ul_valid.is_valid())
    print()

    ul_invalid = Ul([P(Text("Not Li"))])
    page_ul_invalid = Page(ul_invalid)
    print("Invalid Ul test (not Li):")
    print("is_valid():", page_ul_invalid.is_valid())
    print()

    table_valid = Table([Tr([Td(Text("Cell"))])])
    page_table_valid = Page(table_valid)
    print("Valid Table test:")
    print("is_valid():", page_table_valid.is_valid())
    print()

    table_invalid = Table([P(Text("Not Tr"))])
    page_table_invalid = Page(table_invalid)
    print("Invalid Table test (not Tr):")
    print("is_valid():", page_table_invalid.is_valid())
    print()

    page.write_to_file("/invalid/path/test.html")
    print("Tested write_to_file with invalid path")
