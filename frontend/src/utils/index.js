const getToken = () => {
  return localStorage.getItem('token')
}

const setToken = (token) => {
  if (token) {
    localStorage.setItem('token', token);
    localStorage.setItem('userdata', atob(token.split('.')[1]))
  }
}

const removeToken = () => {
  localStorage.removeItem('token');
  localStorage.removeItem('userdata');
}

const getUserData = () => {
  return JSON.parse(localStorage.getItem('userdata'))
}

export {
  getToken,
  setToken,
  removeToken,
  getUserData,
}