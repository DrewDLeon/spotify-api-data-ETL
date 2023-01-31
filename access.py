CLIENT_ID = '83abd770c12e4e16b294c6f30922e83f'
CLIENT_SECRET = 'dfb5fc67f97944f09eaae3b7214f2469'
'''
El redirect URI requiere de estar codificado con un URL Encoder
'''
redirect_uri = 'https%3A%2F%2Fdrewdleon.github.io'

##REQUEST USER AUTHORIZATION
request_user_auth_url = 'https://accounts.spotify.com/authorize?client_id=83abd770c12e4e16b294c6f30922e83f&response_type=code&redirect_uri=https%3A%2F%2Fdrewdleon.github.io&scope=playlist-modify-public%20playlist-modify-private'


code = 'AQD51PYT91rD15iZkOvsjtqXYwy5pv7OQDozUbpy4aU4xJzsdFCvXu2zDrXGh7BUz3MGxjyHZqHU5cziDNVmCZgDgAmQ6lId5BiaRRNffp_UYRFMaPYTtUXsnioddoHk7EKhkB_LgQ81T1J0WSI8bROZPtCQ8gzP9l8fRuVz3s12bRM6K-mg6nVTIO-uURqUembH4f4HgmKMUGFMPebYJpuJudGeVs5xpIfJ1AlT0YY'

##REQUEST ACCESS TOKEN
request_access_token_url = 'https://accounts.spotify.com/api/token?grant_type=authorization_code&code=AQClNGz7FoEAsW6e2y5ze07qjtstWYle0k71NnFdT8xft6EHhwit_BXe-5Gc_PlmxxXk4Eheo8ae8jzgNKodPyAkbuoA8kFhLfUP9bM24dJnRULwbqctgH7m1F7QJGWn5r0DJed6jbdDujWVDQg7ADoPy8C0CkN3z-Zezoh3TMS4rIGZ2SsuOecuHgvUCU88u6TPhXWCgoC9I48VpVQC_ibWMrmiVlL6ev_PQSgujgU&redirect_uri=https%3A%2F%2Fdrewdleon.github.io'
request_access_token_headers = {
    'Authorization' : 'Basic ODNhYmQ3NzBjMTJlNGUxNmIyOTRjNmYzMDkyMmU4M2Y6ZGZiNWZjNjdmOTc5NDRmMDllYWFlM2I3MjE0ZjI0Njk=',
    'Content-Type' : 'application/x-www-form-urlencoded'
}

#curl -H "Authorization: Basic ODNhYmQ3NzBjMTJlNGUxNmIyOTRjNmYzMDkyMmU4M2Y6ZGZiNWZjNjdmOTc5NDRmMDllYWFlM2I3MjE0ZjI0Njk=" -d grant_type=authorization_code -d code=AQD51PYT91rD15iZkOvsjtqXYwy5pv7OQDozUbpy4aU4xJzsdFCvXu2zDrXGh7BUz3MGxjyHZqHU5cziDNVmCZgDgAmQ6lId5BiaRRNffp_UYRFMaPYTtUXsnioddoHk7EKhkB_LgQ81T1J0WSI8bROZPtCQ8gzP9l8fRuVz3s12bRM6K-mg6nVTIO-uURqUembH4f4HgmKMUGFMPebYJpuJudGeVs5xpIfJ1AlT0YY -d redirect_uri=https%3A%2F%2Fdrewdleon.github.io https://accounts.spotify.com/api/token --ssl-no-revoke
