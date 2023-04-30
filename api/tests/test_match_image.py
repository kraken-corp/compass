from utils import match_image

def test_match_island():
    best_match = match_image.match_island('test1.png')
    assert best_match['Name'] == 'Shipwreck Bay'