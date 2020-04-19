#### Release 0.0.15
- add a param converters in as_dict function, which means u can do the convertion according to your requirements. the format for this param is {'key': func}
- add bulk_query decorator, so you can insert multiple rows to the db
- add as_df function to the RecordCollection

#### Release 0.0.14
- Fix the initialize issue in the way like FlaskRecords()
- Modified the error in the Doc

#### Release 0.0.9
- Support the default params in the function when do the query
- Compatible with the Python2.7+ and 3.5+

#### Release 0.0.8
- Support the decorators on the function or method in the class
- Simplify the usage of the decorators
- Provide the base crud operations
- Add unit tests for the decorators, basic dao etc
