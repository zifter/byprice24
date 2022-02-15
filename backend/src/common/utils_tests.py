from common.utils import cleanup_url


def test_cleanup_url_ok():
    url = 'https://www.funtastik.by:443/igrushki/konstruktory/konstruktor-lego-minecraft-21164-korallovyy-rif/?utm_source=yandex&yclid=601272390574470559&utm_medium=cpc&utm_campaign=dinamicheskie_smotreli_na_nashem_sajte_YAD_rsya&utm_term=&utm_content=%7Bcreative%7D%2F%7Bmatchtype%7D%2F%7Badposition%7D%2F%7Bdevice%7D%2F%7Bdevicemodel%7D'
    expected = 'https://www.funtastik.by/igrushki/konstruktory/konstruktor-lego-minecraft-21164-korallovyy-rif/'
    assert cleanup_url(url) == expected

    url = 'https://www.funtastik.by:443/igrushki/konstruktory/?yclid=601272390574470559&q=2'
    expected = 'https://www.funtastik.by/igrushki/konstruktory/?q=2'
    assert cleanup_url(url) == expected

    url = 'https://www.funtastik.by/igrushki/?q=2'
    assert cleanup_url(url) == url

    url = 'https://www.funtastik.by/igrushki/'
    assert cleanup_url(url) == url
