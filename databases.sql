CREATE TABLE products
(
    id              SERIAL PRIMARY KEY,
    shop_id         BIGINT,
    name            VARCHAR(255),
    description     TEXT,
    thumbnail_url   TEXT NOT NULL,
    origin_price    BIGINT NOT NULL,
    discounted_price BIGINT NOT NULL,
    discounted_rate FLOAT,
    status          VARCHAR(191) NOT NULL,
    in_stock        BOOLEAN DEFAULT FALSE,
    is_preorder     BOOLEAN DEFAULT FALSE,
    is_purchasable  BOOLEAN DEFAULT FALSE,
    delivery_condition VARCHAR(255) NOT NULL,
    delivery_display TEXT,
    created_at      TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at      TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL
);

CREATE TABLE favorites
(
    id           SERIAL PRIMARY KEY,
    user_id      BIGINT REFERENCES users(id) ON DELETE CASCADE,
    product_id   BIGINT REFERENCES products(id) ON DELETE CASCADE,
    created_at   TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CONSTRAINT unique_favorite UNIQUE (user_id, product_id)
);

CREATE TABLE users
(
    id          BIGINT AUTO_INCREMENT PRIMARY KEY,
    name        VARCHAR(50),
    email       VARCHAR(50),
    password    VARCHAR(255),
    phone       VARCHAR(50),
    status      VARCHAR(191) NOT NULL,
    created_at  DATETIME(3) NOT NULL,
    updated_at  DATETIME(3) NOT NULL,
    deleted_at  DATETIME(3),
    CONSTRAINT users_email_uindex UNIQUE (email)
);
