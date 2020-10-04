import {ref ,readonly} from 'vue'
import axios from 'axios';
import {getToken} from '../utils';

export const useAxios = async (url, data) => {
  const checkIfdata = (data) => typeof(data) === 'object';
  const axiosConfig = {
    method: checkIfdata(data) ? 'POST': 'GET',
    url,
    headers: { 'Authorization': `Bearer ${getToken()}` },
    ...(checkIfdata(data) ? {data} : {})
  }
  try {
    return await axios(axiosConfig);
  } catch(err) {
    console.log(err);
  }
}