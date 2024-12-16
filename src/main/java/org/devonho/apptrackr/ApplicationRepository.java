package org.devonho.apptrackr;

import java.util.List;

import org.springframework.data.mongodb.repository.MongoRepository;

public interface ApplicationRepository extends MongoRepository<Application, String> {
       

}
