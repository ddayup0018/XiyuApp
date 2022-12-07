import {getRequest, postRequest, putRequest,deleteRequest} from "@/utils/http"

export function deletetaocan(id){
    return deleteRequest(`/taocan/${id}/`)
}

export const taocan = {
    delete(id){
        return deleteRequest(`/taocan/${id}`)
    },
    get(id=''){
        return getRequest(`/taocan/${id}`)
    },
    post(data){
        return postRequest(`/taocan/`,data)
    },
    put(id,data){
        return putRequest(`/taocan/${id}/`,data)
    }
}