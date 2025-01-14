import jwt from 'jsonwebtoken';

const SECRET = process.env.JWT_SECRET || "RAS2025"; 

function verifyToken(token, res, callback) {
  jwt.verify(token, SECRET, function (err, payload) {
    if (err) {
      res.status(401).jsonp({ error: "Token inválido ou expirado." });
    } else {
      callback(payload);
    }
  });
}

module.exports.verificaAcesso = function (req, res, next) {
  var myToken = req.body.token || req.query.token;
  if (myToken) {
    verifyToken(myToken, res, (payload) => {
      req.user = payload;
      req.token = myToken;
      next();
    });
  } else {
    res.status(401).jsonp({ error: "Token inexistente!" });
  }
};
