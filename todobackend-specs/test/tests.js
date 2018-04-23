const chai = require('chai')
const should = chai.should;
const expect = chai.expect;
const promise = require('bluebird')
const request = require('superagent-promise')(require('superagent'),promise);
const chaiPromise = require('chai-as-promised');

chai.use(chaiPromise)

var url = process.env.URL || 'http://localhost:8000/todos';


describe('cross origin request',function(){
  var result ;
  before(function(){
    result = request('OPTIONS',url)
    .set('Origin','http://someplace.com')
    .end();
  });
  it('should return the correct CORS headers',function(){
    return assert(result,'header').to.contain.all.keys([
      'access-control-allow-origin',
      'access-control-allow-methods',
      'access-control-allow-headers'
    ]);
  });

  it('should allow all origins', function(done){
    result.then(data=>{
      expect(data['header']['access-control-allow-origin']).to.equal('*')
      done()
    })
  })
});


describe('create todo item',function(){
  var result ;
  before(function(){
    result = post(url,{title:'walk the dog'});
  });
  it('should return a 201 created response',function(){
    return assert(result,'status').to.equal(201);
  });

  it('should receive a location hyperlink', function(done){
    result.then(data=>{
      expect(data['header']['location']).to.match(/^https?:\/\/.+\/todos\/[\d]+$/);
      done()
    })
  })

  it('should create one item',function(done){
    var item = result.then(function(res){
      return get(res.header['location']);
    });
    result.then(data=>{
      expect(data['body']['title']).to.equal("walk the dog");
      done()
    })
  })
  after(function(){
    return del(url)
  })
});

describe('update todo item',function(){
  var location ;
  beforeEach(function(done){
    result = post(url,{title:'walk the dog'}).then(function(res){
      location = res.header['location'];
      done()
    });
  });
  it('should have completed set to true after put update',function(done){
    // return assert(result,'status').to.equal(201);
    var result = update(location,'PUT',{'completed':true})
    result.then(data=>{
      expect(data['body']['completed']).to.be.true;
      done()
    })
  });

  it('should have completed set to true after patch update',function(done){
    // return assert(result,'status').to.equal(201);
    var result = update(location,'PATCH',{'completed':true})
    result.then(data=>{
      expect(data['body']['completed']).to.be.true;
      done()
    })
    // return assert(result,'body.completed').to.be.true;
  });
  after(function(){
    return del(url)
  })
});

describe('delete todo item',function(){
  var location ;
  beforeEach(function(done){
    result = post(url,{title:'walk the dog'}).then(function(res){
      location = res.header['location'];
      done()
    });
  });
  it('should return 204 no content response',function(){
    // return assert(result,'status').to.equal(201);
    var result = del(location)
    return assert(result,'status').to.equal(204);
  });

  it('should delete the item',function(){
    // return assert(result,'status').to.equal(201);
    var result = del(location).then(function(res){
      return get(location);
    })
    return expect(result).to.eventually.be.rejectedWith('Not Found');
  });
});




const post = function(url,data){
  return request.post(url)
  .set('Content-Type','application/json')
  .set('Accept','application/json')
  .send(data)
  .end();
}

const get = function(url){
  return request.get(url)
  .set('Accept','application/json')
  .end();
}
const del = function(url){
  return request.del(url)
  .end();
}
const update = function(url,method,data){
  return request(method,url)
  .set('Content-Type','application/json')
  .set('Accept','application/json')
  .send(data)
  .end();
}

function assert(result,prop){
  return expect(result).to.eventually.have.deep.property(prop);
}