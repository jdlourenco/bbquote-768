from bbquote.lib import get_quote

def test_get_quote():
    res = get_quote()
    assert type(res) == str
    assert len(res) >= 0
