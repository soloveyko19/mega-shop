export interface credentials {
    username: string,
    password: string
}

export interface profile {
    username: string,
    id: number
}

export interface category {
    id: number,
    name: string
}

export interface product {
    title: string,
    price: number,
    description: string,
    image_url: string,
    category_id: number
}

export type categoryList = Array<category>

export type requestStatus = 'idle' | 'pending' | 'success' | 'error'
