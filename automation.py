import pyautogui
import time
import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


data = ['[32]', 'Sed', 'ut', 'perspiciatis,', 'unde', 'omnis', 'iste', 'natus', 'error', 'sit', 'voluptatem', 'accusantium', 'doloremque', 'laudantium,', 'totam', 'rem', 'aperiam', 'eaque', 'ipsa,', 'quae', 'ab', 'illo', 'inventore', 'veritatis', 'et', 'quasi', 'architecto', 'beatae', 'vitae', 'dicta', 'sunt,', 'explicabo.', 'Nemo', 'enim', 'ipsam', 'voluptatem,', 'quia', 'voluptas', 'sit,', 'aspernatur', 'aut', 'odit', 'aut', 'fugit,', 'sed', 'quia', 'consequuntur', 'magni', 'dolores', 'eos,', 'qui', 'ratione', 'voluptatem', 'sequi', 'nesciunt,', 'neque', 'porro', 'quisquam', 'est,', 'qui', 'dolorem', 'ipsum,', 'quia', 'dolor', 'sit', 'amet', 'consectetur', 'adipisci[ng]', 'velit,', 'sed', 'quia', 'non', 'numquam', '[do]', 'eius', 'modi', 'tempora', 'inci[di]dunt,', 'ut', 'labore', 'et', 'dolore', 'magnam', 'aliquam', 'quaerat', 'voluptatem.', 'Ut', 'enim', 'ad', 'minima', 'veniam,', 'quis', 'nostrum[d]', 'exercitationem', 'ullam', 'corporis', 'suscipit', 'laboriosam,', 'nisi', 'ut', 'aliquid', 'ex', 'ea', 'commodi', 'consequatur?', '[D]Quis', 'autem', 'vel', 'eum', 'iure', 'reprehenderit,', 'qui', 'in', 'ea', 'voluptate', 'velit', 'esse,', 'quam', 'nihil', 'molestiae', 'consequatur,', 'vel', 'illum,', 'qui', 'dolorem', 'eum', 'fugiat,', 'quo',
        'voluptas', 'nulla', 'pariatur?', '[33]', 'At', 'vero', 'eos', 'et', 'accusamus', 'et', 'iusto', 'odio', 'dignissimos', 'ducimus,', 'qui', 'blanditiis', 'praesentium', 'voluptatum', 'deleniti', 'atque', 'corrupti,', 'quos', 'dolores', 'et', 'quas', 'molestias', 'excepturi', 'sint,', 'obcaecati', 'cupiditate', 'non', 'provident,', 'similique', 'sunt', 'in', 'culpa,', 'qui', 'officia', 'deserunt', 'mollitia', 'animi,', 'id', 'est', 'laborum', 'et', 'dolorum', 'fuga.', 'Et', 'harum', 'quidem', 'rerum', 'facilis', 'est', 'et', 'expedita', 'distinctio.', 'Nam', 'libero', 'tempore,', 'cum', 'soluta', 'nobis', 'est', 'eligendi', 'optio,', 'cumque', 'nihil', 'impedit,', 'quo', 'minus', 'id,', 'quod', 'maxime', 'placeat,', 'facere', 'possimus,', 'omnis', 'voluptas', 'assumenda', 'est,', 'omnis', 'dolor', 'repellendus.', 'Temporibus', 'autem', 'quibusdam', 'et', 'aut', 'officiis', 'debitis', 'aut', 'rerum', 'necessitatibus', 'saepe', 'eveniet,', 'ut', 'et', 'voluptates', 'repudiandae', 'sint', 'et', 'molestiae', 'non', 'recusandae.', 'Itaque', 'earum', 'rerum', 'hic', 'tenetur', 'a', 'sapiente', 'delectus,', 'ut', 'aut', 'reiciendis', 'voluptatibus', 'maiores', 'alias', 'consequatur', 'aut', 'perferendis', 'doloribus', 'asperiores', 'repellat.\n']


def simulate_kaggle():
    blank = Point(x=902, y=157)
    pyautogui.moveTo(blank.x, blank.y)
    pyautogui.click()

    mover = Point(x=1611, y=903)
    pyautogui.scroll(-2000, x=mover.x, y=mover.y)

    cell = Point(x=200, y=960)
    pyautogui.click(cell.x, cell.y)
    pyautogui.click(cell.x, cell.y)
    time.sleep(1)
    pyautogui.write('print("hello world!")', interval=1)
    pyautogui.hotkey('shift', 'enter')


def simulate_colab():
    blank = Point(x=870, y=161)
    pyautogui.moveTo(blank.x, blank.y)
    pyautogui.click()

    mover = Point(x=1916, y=647)
    pyautogui.scroll(-2000, x=mover.x, y=mover.y)

    cell = Point(x=417, y=617)
    pyautogui.click(cell.x, cell.y)
    pyautogui.click(cell.x, cell.y)
    time.sleep(1)
    pyautogui.write(random.choice(data), interval=0.25)
    pyautogui.hotkey('shift', 'enter')


tabs = [Point(x=126, y=46), Point(x=355, y=44),
        Point(x=597, y=44), Point(x=832, y=41)]

while(True):
    for tab in tabs[:2]:
        pyautogui.click(tab.x, tab.y)
        simulate_colab()
        time.sleep(3)

    min = random.randint(0,20)
    time.sleep(60*min)
