export interface credentials {
    email: string,
    password: string
}

export interface profile {
    email: string,
    id: number
    name: string
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
