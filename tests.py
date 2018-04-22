from main import read_srt, merge_overlapping

def test_simple_srt_block():
    text = """1
00:00:03,100 --> 00:00:03,560
Within the spreading darkness

"""
    expected = {
        'index': "1",
        'start': "00:00:03,100",
        'end': "00:00:03,560",
        'text': "Within the spreading darkness",
    }

    srt_blocks = list(read_srt(text))
    assert srt_blocks == [expected]

def test_multiline_srt_block():
    text = """1
00:00:03,100 --> 00:00:03,560
Within the spreading darkness
Is eternal damnation

"""
    expected = {
        'index': "1",
        'start': "00:00:03,100",
        'end': "00:00:03,560",
        'text': "Within the spreading darkness\nIs eternal damnation",
    }

    srt_blocks = list(read_srt(text))
    assert srt_blocks == [expected]


def test_merge_overlapping_one():
    srt_blocks = [
        { 'index': '1', 'start': "00:00:03,100", 'end': "00:00:03,560", 'text': "foo" },
    ]

    assert list(merge_overlapping(srt_blocks)) == srt_blocks


def test_merge_overlapping_two():
    srt_blocks = [
        { 'index': '1', 'start': "00:00:03,100", 'end': "00:00:03,560", 'text': "foo" },
        { 'index': '2', 'start': "00:00:03,400", 'end': "00:00:03,800", 'text': "bar" },
    ]
    expected = [
        { 'index': '1', 'start': "00:00:03,100", 'end': "00:00:03,800", 'text': "foo\nbar" },
    ]

    assert list(merge_overlapping(srt_blocks)) == expected

def test_expand_same_text():
    srt_blocks = [
        { 'index': '1', 'start': "00:00:03,100", 'end': "00:00:03,560", 'text': "foo" },
        { 'index': '2', 'start': "00:00:03,400", 'end': "00:00:03,800", 'text': "foo" },
    ]
    expected = [
        { 'index': '1', 'start': "00:00:03,100", 'end': "00:00:03,800", 'text': "foo" },
    ]

    assert list(merge_overlapping(srt_blocks)) == expected