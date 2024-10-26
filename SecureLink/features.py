from . import utils
import re

class FeatureExtractor:
    def extract_features(self, url):
        """Extract features from URL"""
        url = utils.preprocess_url(url)
        parsed = utils.urlparse(url)

        features = {
            # URL-based features
            'url_length': len(url),
            'domain_length': len(parsed.netloc),
            'dots_count': url.count('.'),
            'special_chars': sum(c in '~!@#$%^&*()_+=[]{}|;:,.<>?' for c in url),
            'has_ip': bool(re.match(r'\\d+\\.\\d+\\.\\d+\\.\\d+', parsed.netloc)),
            'has_at_symbol': '@' in url,
            'has_double_slash': '//' in url[8:],
            'has_dash': '-' in parsed.netloc,
            'subdomain_count': len(parsed.netloc.split('.')) - 1,

            # Path-based features
            'path_length': len(parsed.path),
            'path_depth': len([x for x in parsed.path.split('/') if x]),
            'has_suspicious_words': self._check_suspicious_words(url),
            'query_length': len(parsed.query),
            'fragment_length': len(parsed.fragment),
        }

        return features

    def _check_suspicious_words(self, url):
        """Check for common suspicious words"""
        suspicious = ['login', 'signin', 'verify', 'secure', 'account', 'update', 'confirm']
        return any(word in url.lower() for word in suspicious)

