module.exports = (function(){
	return{
	 local: {
	 	host: 'localhost',
		port: '3306',
		user: 'root',
		password: '2021',
		database: 'bigdata'
	 },
	 prod: {
		host: '',
		port: '',
		user: '',
		password: '!',
		database: ''
	 },
	 dev: {
		host: '',
		port: '',
		user: '',
		password: '',
		database: ''
	 }
	}
})();
