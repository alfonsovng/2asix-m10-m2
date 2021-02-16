DELETE FROM public.departments;

INSERT INTO public.departments VALUES (1, 'Marketing');
INSERT INTO public.departments VALUES (2, 'Finance');
INSERT INTO public.departments VALUES (3, 'Human Resources');
INSERT INTO public.departments VALUES (4, 'Production');
INSERT INTO public.departments VALUES (5, 'Development');
INSERT INTO public.departments VALUES (6, 'Quality Management');
INSERT INTO public.departments VALUES (7, 'Sales');
INSERT INTO public.departments VALUES (8, 'Research');
INSERT INTO public.departments VALUES (9, 'Customer Service');

SELECT pg_catalog.setval('public.departments_id_seq', 9, true);
