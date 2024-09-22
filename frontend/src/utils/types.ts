export interface credentials {
    username: string,
    password: string
}

export interface profile {
    username: string,
    id: number
}


export type requestStatus = 'idle' | 'pending' | 'success' | 'error'