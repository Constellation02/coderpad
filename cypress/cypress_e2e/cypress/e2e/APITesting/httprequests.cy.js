// petStoreTests.spec.js

describe('PetStore API tests', () => {
  const petId = 123456789; // ID de la mascota definido manualmente

  it('Añadir una mascota a la tienda con ID específico', () => {
    cy.request({
      method: 'POST',
      url: 'https://petstore.swagger.io/v2/pet',
      body: {
        "id": petId,
        "category": {
          "id": 0,
          "name": "dog"
        },
        "name": "doggie",
        "photoUrls": [
          "string"
        ],
        "tags": [
          {
            "id": 0,
            "name": "tag1"
          }
        ],
        "status": "available"
      }
    }).then((response) => {
      expect(response.status).to.eq(200);
      expect(response.body.id).to.eq(petId);
    });
  });

  it('Consultar la mascota ingresada previamente (Búsqueda por ID)', () => {
    cy.request({
      method: 'GET',
      url: `https://petstore.swagger.io/v2/pet/${petId}`
    }).then((response) => {
      expect(response.status).to.eq(200);
      expect(response.body.id).to.eq(petId);
    });
  });

  it('Actualizar el nombre de la mascota y el estatus a "sold"', () => {
    cy.request({
      method: 'PUT',
      url: 'https://petstore.swagger.io/v2/pet',
      body: {
        "id": petId,
        "category": {
          "id": 0,
          "name": "dog"
        },
        "name": "doggieUpdated",
        "photoUrls": [
          "string"
        ],
        "tags": [
          {
            "id": 0,
            "name": "tag2"
          }
        ],
        "status": "sold"
      }
    }).then((response) => {
      expect(response.status).to.eq(200);
      expect(response.body.name).to.eq('doggieUpdated');
      expect(response.body.status).to.eq('sold');
    });
  });

  it('Consultar la mascota modificada por estatus (Búsqueda por estatus)', () => {
    cy.request({
      method: 'GET',
      url: 'https://petstore.swagger.io/v2/pet/findByStatus?status=sold'
    }).then((response) => {
      expect(response.status).to.eq(200);
      // Verificar que la respuesta incluya la mascota actualizada
      expect(response.body.some(pet => pet.id === petId && pet.status === 'sold')).to.be.true;
    });
  });
});
