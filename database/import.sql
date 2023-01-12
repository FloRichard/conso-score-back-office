
-- Creating category of products
insert into public.category (category_id, name, threshold) values ('57857a10-6182-4377-843d-01f90dfe27f9', 'Viande', 20);
insert into public.category (category_id, name, threshold) values ('9fa21198-325a-4f8b-9800-6cbe84346bb4', 'Légumes', 40);


-- Creating expedition transports
insert into public.expedition_transport (expedition_transport_id, name, kilometer_carbon_footprint) values ('7416fd36-b450-4fe4-a777-5e033fef7c70', 'Camion', 0.12);
insert into public.expedition_transport (expedition_transport_id, name, kilometer_carbon_footprint) values ('00f95a18-4736-484e-9a3d-f23703fb95c8', 'Voiture', 0.251);

-- Creating maker products
insert into public.product (product_id, name, price, carbon_footprint, quantity_unity, category_id, expedition_transport_id) values ('588c72f7-65e3-4d41-93e7-31cea19fce2d','Côte de Boeuf', 34.5, 200, 'Kg', '57857a10-6182-4377-843d-01f90dfe27f9', '7416fd36-b450-4fe4-a777-5e033fef7c70');
insert into public.product (product_id, name, price, carbon_footprint, quantity_unity, category_id, expedition_transport_id) values ('87a1e36f-c193-4640-ba98-fd8dd58e25ce','Carrote', 1, 100, 'Kg', '9fa21198-325a-4f8b-9800-6cbe84346bb4', '00f95a18-4736-484e-9a3d-f23703fb95c8');

-- Creating the seller products
insert into public.seller_product (seller_product_id , product_id, price, conso_score, bar_code, tax) values ('ddafae54-a96c-4b3d-95ea-8ff3e6ef0d71', '588c72f7-65e3-4d41-93e7-31cea19fce2d', 40, 67, '1234', 15);
insert into public.seller_product (seller_product_id , product_id, price, conso_score, bar_code, tax) values ('cd6d6cc4-0775-4749-b9b7-bc6e5eed9e1b', '87a1e36f-c193-4640-ba98-fd8dd58e25ce', 2, 15, '4321', 0);

-- Creating a seller 
insert into public.seller(seller_id, name, location) values ('5a39c805-4e15-4944-80af-333d2d11bced', 'Jean Dupont POS', '24 rue Lanfranc, 14000, Caen');

-- Creating a maker
insert into public.maker(maker_id, name, location) values ('5503a140-ab18-4d1a-8b17-3356e8e01a80', 'George fruit et legume', '22 Rue de la Vallée, 14100 Lisieux');

-- Creating seller stock with 2 products
insert into public.seller_stock (seller_stock_id, seller_product_id, seller_id, quantity) values ('6aa5a9e3-6d47-4810-aaab-31e26ddf969d', 'ddafae54-a96c-4b3d-95ea-8ff3e6ef0d71','5a39c805-4e15-4944-80af-333d2d11bced', 2);
insert into public.seller_stock (seller_stock_id, seller_product_id, seller_id, quantity) values ('6aa5a9e3-6d47-4810-aaab-31e26ddf969d', 'cd6d6cc4-0775-4749-b9b7-bc6e5eed9e1b','5a39c805-4e15-4944-80af-333d2d11bced', 3);

-- Creating maker stock 
insert into public.maker_stock (maker_stock_id, product_id, maker_id) values ('6aa5a9e3-6d47-4810-aaab-31e26ddf969d', '588c72f7-65e3-4d41-93e7-31cea19fce2d','5503a140-ab18-4d1a-8b17-3356e8e01a80');
insert into public.maker_stock (maker_stock_id, product_id, maker_id) values ('6aa5a9e3-6d47-4810-aaab-31e26ddf969d', '87a1e36f-c193-4640-ba98-fd8dd58e25ce','5503a140-ab18-4d1a-8b17-3356e8e01a80');



-- Creating the partnership between the seller and the maker
insert into public.partnership (maker_id, seller_id) values ('5503a140-ab18-4d1a-8b17-3356e8e01a80', '5a39c805-4e15-4944-80af-333d2d11bced');

-- Creating status of user seller 
insert into public.status (status_id, maker_id, seller_id, label) values ('7ec56444-6df0-4f8a-a154-822858d990af', null, '5a39c805-4e15-4944-80af-333d2d11bced', 'SELLER');

-- Creating status user maker 
insert into public.status (status_id, maker_id, seller_id, label) values ('3a0e5e5e-c861-4e8a-a4a4-01ef2972eec8', '5503a140-ab18-4d1a-8b17-3356e8e01a80', null, 'MAKER');

-- Creating user (he is a seller)
insert into public.user (user_id, status_id, name, login, password) values ('b550312d-b519-4083-8440-34af067d7949', '7ec56444-6df0-4f8a-a154-822858d990af', 'Jean Dupont', 'jeanDupont', 'mypassword');

-- Creating user (he is a maker)
insert into public.user (user_id, status_id, name, login, password) values ('b0b3a3d2-1342-4a0d-8607-05ac9388051d', '3a0e5e5e-c861-4e8a-a4a4-01ef2972eec8', 'George Blad', 'gbald', 'mypassword');





