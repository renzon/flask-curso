from blueprints.posts.github import avatar


def test_github_api(mocker):
    get_mock = mocker.patch('blueprints.posts.github.requests.get')
    resp = mocker.Mock()
    avatar_url = 'https://avatars3.githubusercontent.com/u/3457115?v=4'
    resp.json.return_value = {'avatar_url': avatar_url}

    get_mock.return_value = resp
    assert avatar('renzon') == avatar_url
    get_mock.assert_called_once_with()
