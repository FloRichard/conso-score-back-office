CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

create table public.user (
    user_id uuid DEFAULT uuid_generate_v4() not null,
    status_id uuid not null,
    name varchar(128) not null,
    login varchar(128) not null,
    password varchar(128) not null,
    constraint pk_user primary key (user_id)
);

create table public.seller (
    seller_id uuid DEFAULT uuid_generate_v4() not null,
    name varchar(128) not null,
    location varchar(128) not null,
    constraint pk_seller primary key (seller_id)
);

create table public.maker (
    maker_id uuid DEFAULT uuid_generate_v4() not null,
    name varchar(128) not null,
    location varchar(128) not null,
    constraint pk_maker primary key (maker_id)
);

create table public.partnership (
    maker_id uuid not null,
    seller_id uuid not null,
    constraint pk_partnership primary key (maker_id, seller_id)
);

create table public.status (
    status_id uuid DEFAULT uuid_generate_v4() not null,
    maker_id uuid,
    seller_id uuid,
    label varchar(32) not null,
    constraint pk_status primary key (status_id)
);

create table public.seller_stock (
    seller_stock_id uuid DEFAULT uuid_generate_v4() not null,
    seller_product_id uuid not null,
    seller_id uuid not null,
    quantity int not null,
    constraint pk_seller_stock primary key (seller_stock_id, seller_product_id, seller_id)
);

create table public.seller_product (
    seller_product_id uuid DEFAULT uuid_generate_v4() not null,
    product_id uuid not null,
    price real not null,
    conso_score int,
    bar_code varchar(128) not null,
    tax int,
    constraint pk_seller_product primary key (seller_product_id)
);

create table public.maker_stock (
    maker_stock_id uuid DEFAULT uuid_generate_v4() not null,
    product_id uuid not null,
    maker_id uuid not null,
    constraint pk_maker_stock primary key (maker_stock_id, product_id, maker_id)
);

create table public.product (
    product_id uuid DEFAULT uuid_generate_v4() not null,
    name varchar(128) not null,
    price real not null,
    carbon_footprint real not null,
    quantity_unity varchar(128) not null,
    category_id uuid not null,
    expedition_transport_id uuid not null,
    constraint pk_product primary key (product_id)
);

create table public.category (
    category_id uuid DEFAULT uuid_generate_v4() not null,
    name varchar(128) not null,
    threshold int not null,
    constraint pk_category primary key (category_id)
);

create table public.expedition_transport (
    expedition_transport_id uuid DEFAULT uuid_generate_v4() not null,
    name varchar(128) not null,
    kilometer_carbon_footprint real not null,
    constraint pk_expedition_transport primary key (expedition_transport_id)
);


-- User foreign keys
alter table public.user add
    constraint fk_user_status
        foreign key (status_id)
            references public.status (status_id)
                on delete cascade;

-- Seller foreign keys


-- Maker foreign keys


-- Partnership foreign keys
alter table public.partnership add
    constraint fk_partnership_maker
        foreign key (maker_id)
            references public.maker (maker_id)
                on delete cascade;

alter table public.partnership add
    constraint fk_partnership_seller
        foreign key (seller_id)
            references public.seller (seller_id)
                on delete cascade;

-- Status foreign keys
alter table public.status add
    constraint fk_status_maker
        foreign key (maker_id)
            references public.maker (maker_id)
                on delete cascade;

alter table public.status add
    constraint fk_status_seller
        foreign key (seller_id)
            references public.seller (seller_id)
                on delete cascade;

-- Seller stock foreign keys 
alter table public.seller_stock add
    constraint fk_seller_stock_seller_product
        foreign key (seller_product_id)
            references public.seller_product (seller_product_id)
                on delete cascade;

alter table public.seller_stock add
    constraint fk_seller_stock_seller
        foreign key (seller_id)
            references public.seller (seller_id)
                on delete cascade;

-- Seller product foreign keys
alter table public.seller_product add
    constraint fk_seller_product_product
        foreign key (product_id)
            references public.product (product_id)
                on delete cascade;

-- Product foreign keys
alter table public.product add
    constraint fk_product_category
        foreign key (category_id)
            references public.category (category_id)
                on delete cascade;

alter table public.product add
    constraint fk_product_expedition_transport
        foreign key (expedition_transport_id)
            references public.expedition_transport (expedition_transport_id)
                on delete cascade;

-- Maker stock foreign keys 
alter table public.maker_stock add
    constraint fk_maker_stock_maker_product
        foreign key (product_id)
            references public.product (product_id)
                on delete cascade;

alter table public.maker_stock add
    constraint fk_maker_stock_maker
        foreign key (maker_id)
            references public.maker (maker_id)
                on delete cascade;